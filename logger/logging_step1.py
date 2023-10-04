import logging


class LoggingDemo1:
    logging.basicConfig(level=logging.INFO)

    def test_method_1(self):
        logging.info("Executing test_method_1")

    def test_method_2(self):
        logging.info("Executing test_method_2")


obj = LoggingDemo1()
obj.test_method_1()
obj.test_method_2()
