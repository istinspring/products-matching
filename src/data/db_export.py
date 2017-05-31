# -*- coding: utf-8 -*-
import os
import csv
import logging

import click
from pymongo import MongoClient


logger = logging.getLogger(__name__)
db = MongoClient()['stores']
project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)


@click.group()
def cmd():
    pass


@cmd.command()
def sizes():
    logger.info("Run aggregation...")
    results = db.data.aggregate(
        [
            {
                "$group": {
                    "_id": "$size",
                    "count": {"$sum": 1}
                },
            },
            {
                "$sort": {
                    "count": -1,
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "count": 1,
                }
            }
        ]
    )
    count = len(db.data.distinct("size"))
    logger.info("Aggregation done.")

    filename = os.path.join(project_dir, 'data/interim/sizes_with_freq.csv')
    with open(filename, 'w') as f:
        logger.info("Export results into the csv file...")
        fieldnames = ['name', 'resolve_to', 'frequency']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        with click.progressbar(
                length=count, show_pos=True, label='Rows') as row:
            for res in results:
                writer.writerow(
                    {
                        "name": res["_id"],
                        "resolve_to": "",
                        "frequency": res["count"]
                    }
                )
                row.update(1)
    logger.info("Export done.")


@cmd.command()
def codes():
    logger.info("Run aggregation...")
    results = db.data.aggregate(
        [
            {
                "$group": {
                    "_id": "$code",
                    "count": {"$sum": 1}
                },
            },
            {
                "$sort": {
                    "count": -1,
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "count": 1,
                }
            }
        ]
    )
    count = len(db.data.distinct("code"))
    logger.info("Aggregation done.")

    filename = os.path.join(project_dir, 'data/interim/codes_with_freq.csv')
    with open(filename, 'w') as f:
        logger.info("Export results into the csv file...")
        fieldnames = ['name', 'resolve_to', 'frequency']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        with click.progressbar(
                length=count, show_pos=True, label='Rows') as row:
            for res in results:
                writer.writerow(
                    {
                        "name": res["_id"],
                        "resolve_to": "",
                        "frequency": res["count"]
                    }
                )
                row.update(1)
    logger.info("Export done.")


@cmd.command()
def categories():
    logger.info("Run aggregation...")
    results = db.data.aggregate(
        [
            {
                "$group": {
                    "_id": "$category",
                    "count": {"$sum": 1}
                },
            },
            {
                "$sort": {
                    "count": -1,
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "count": 1,
                }
            }
        ]
    )
    count = len(db.data.distinct("category"))
    logger.info("Aggregation done.")

    filename = os.path.join(project_dir,
                            'data/interim/categories_with_freq.csv')
    with open(filename, 'w') as f:
        logger.info("Export results into the csv file...")
        fieldnames = ['name', 'resolve_to', 'frequency']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        with click.progressbar(
                length=count, show_pos=True, label='Rows') as row:
            for res in results:
                writer.writerow(
                    {
                        "name": str(res["_id"]).upper(),
                        "resolve_to": "",
                        "frequency": res["count"]
                    }
                )
                row.update(1)
    logger.info("Export done.")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    cmd()
