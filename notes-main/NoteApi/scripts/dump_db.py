import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import json
from sqlalchemy import create_engine, MetaData
from config import Config, BASE_DIR
from api.models.note import NoteModel
from api.models.user import UserModel
import click


@click.command
@click.option('--fixture_name', default="data.json", help='json file name')
def dump_db(fixture_name, path_to_db=Config.SQLALCHEMY_DATABASE_URI
            , models_only=None):
    file_name = BASE_DIR / "fixtures" / fixture_name
    engine = create_engine(path_to_db)
    meta = MetaData()
    meta.reflect(bind=engine)
    result = {}
    for table in meta.sorted_tables:
        if models_only and table.name not in [model.__tablename__ for model in models_only]:
            continue
        result[table.name] = [dict(row) for row in engine.execute(table.select())]

    with open(file_name, "w", encoding="UTF-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    dump_db()
# dump_db(Config.SQLALCHEMY_DATABASE_URI, models_only=[UserModel, NoteModel])
