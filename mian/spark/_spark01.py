from pyspark import SparkConf, SparkContext

if __name__ == '__main__':

    conf = SparkConf() \
        .setMaster("local[*]").setAppName("MyApp")

    sc = SparkContext(conf=conf)

    print(sc)

    sc.stop()