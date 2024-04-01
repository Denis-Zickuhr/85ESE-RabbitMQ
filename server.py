from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table
from json import loads
import consume
from sqlalchemy.exc import SQLAlchemyError

def callback(ch, method, properties, body):
    print('retrieved user from queue')
    user = loads(body)

    insert_user(user)

def insert_user(user):
    try:
        engine = create_engine('mysql://mysql:123456@localhost:3306/systemdb')
        metadata = MetaData()
        metadata.bind = engine
        users_table = Table('users', metadata, autoload_with=engine)

        with engine.connect() as connection:
            ins = users_table.insert().values(
                gender=user['gender'],
                title=user['name']['title'],
                first_name=user['name']['first'],
                last_name=user['name']['last'],
                street_number=user['location']['street']['number'],
                street_name=user['location']['street']['name'],
                city=user['location']['city'],
                state=user['location']['state'],
                country=user['location']['country'],
                postcode=user['location']['postcode'],
                latitude=user['location']['coordinates']['latitude'],
                longitude=user['location']['coordinates']['longitude'],
                timezone_offset=user['location']['timezone']['offset'],
                timezone_description=user['location']['timezone']['description'],
                email=user['email'],
                username=user['login']['username'],
                password=user['login']['password'],
                dob_date=datetime.strptime(user['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                dob_age=user['dob']['age'],
                registered_date=datetime.strptime(user['registered']['date'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                registered_age=user['registered']['age'],
                phone=user['phone'],
                cell=user['cell'],
                id_name=user['id']['name'],
                id_value=user['id']['value'],
                picture_large=user['picture']['large'],
                picture_medium=user['picture']['medium'],
                picture_thumbnail=user['picture']['thumbnail'],
                nationality=user['nat']
            )

            with connection.begin():
                connection.execute(ins)

    except SQLAlchemyError as e:
        with open('error.log', 'a') as f:
            f.write(f"Database error: {e}\n")
        print("Database error:", e)


if __name__ == "__main__":
    queue_name = 'users-queue'

    consume.queue_channel(queue_name, callback)