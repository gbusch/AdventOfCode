from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T


def part1(inp_str):
    """
    >>> inp_str = '''1000
    ... 2000
    ... 3000
    ...
    ... 4000'''
    >>> part1(inp_str)
    6000
    """
    df = get_ordered_calories(inp_str)
    return df.limit(1).collect()[0].elf_calories


def part2(inp_str):
    """
    >>> inp_str = '''1
    ... 2
    ... 3
    ...
    ... 4
    ...
    ... 5
    ... 6
    ...
    ... 7
    ... 8
    ... 9
    ...
    ... 10'''
    >>> part2(inp_str)
    45
    """
    df = get_ordered_calories(inp_str)
    return (
        df.limit(3)
        .groupBy()
        .agg(F.sum("elf_calories").alias("calories_sum"))
        .collect()[0]
        .calories_sum
    )


def get_spark():
    return SparkSession.builder.getOrCreate()


def get_ordered_calories(inp_str):
    spark = get_spark()
    df = spark.createDataFrame([[inp_str]], schema="input string")
    df = df.select(F.posexplode(F.split("input", "\n\n")).alias("elf", "calories_list"))
    df = df.select("elf", F.explode(F.split("calories_list", "\n")).alias("calories"))
    return (
        df.groupBy("elf")
        .agg(F.sum("calories").cast(T.IntegerType()).alias("elf_calories"))
        .orderBy(F.desc("elf_calories"))
    )


if __name__ == "__main__":
    with open("data/day01.txt", "r") as f:
        inp_str = f.read()

    print("part 1")
    print(part1(inp_str))

    print("part 2")
    print(part2(inp_str))
