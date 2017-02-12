# The objective of this problem is to implement a connection pool,
#  which is useful when you have connections to a database or other resource that are expensive to open and close.
# When that is the case, you want to re-use those connections as much as possible.
# The class ConnectionConsumer represents this type of expensive connection.
# The overall goal is minimize the number of ConnectionConsumer objects that are opened and closed,
# and the class ConnectionPool, which you need to write, is responsible for making that happen.
#   Feel free to add whatever methods or classes you need inside ConnectionPool.
#  You just need to make all the tests pass.



class ConnectionPool:

    def __init__(self, factory):
        self._factory=factory
        self.connection_list=[]
        class WrapperConnection():
            def __init__(self, connection):
                self._closed = False
                self.connection = connection

            def query(self):
                return self.connection.query()

            def close(self):
                self._closed = True
                self.connection._closed = True

            def restart(self):
                self._closed = False
                self.connection._closed = False
        self._HiddenConnection = WrapperConnection

    def get_connection(self):
        for connection in self.connection_list:
            if connection._closed is True:
                connection.restart()
                return connection
        new_connection= self._HiddenConnection(factory.get_connection())
        self.connection_list.append(new_connection)
        return new_connection




# ================================================================= #
# ==================== DO NOT TOUCH BELOW HERE ==================== #
# ================================================================= #
class ThirdPartyConnectionException(Exception):
    pass


class ThirdPartyConnectionFactory:
    def __init__(factory):
        factory._open_connections = 0
        factory._opened_connections = 0

        class HiddenConnection:
            def __init__(self):
                self._closed = False
                factory._open_connections += 1
                factory._opened_connections += 1

            def query(self):
                if self._closed:
                    raise ThirdPartyConnectionException()
                return 'Hello, World'

            def close(self):
                self._closed = True
                factory._open_connections -= 1

        factory._HiddenConnection = HiddenConnection

    def get_connection(self):
        return self._HiddenConnection()


class ConnectionConsumer:
    def __init__(self, factory):
        self._factory = factory

    def open(self):
        return self._factory.get_connection()

    def assert_open(self, connection):
        assert connection.query() == 'Hello, World'

    def assert_closed(self, connection):
        try:
            connection.query()
            raise Exception('connection should have been closed')
        except ThirdPartyConnectionException:
            pass

    def cycle_new_connection(self):
        connection = self.open()
        self.assert_open(connection)
        connection.close()
        self.assert_closed(connection)



# Test 1
factory = ThirdPartyConnectionFactory()
consumer = ConnectionConsumer(factory)
consumer.cycle_new_connection()
consumer.cycle_new_connection()

assert factory._open_connections == 0
assert factory._opened_connections == 2
print 'Test 1 passing!'

# Test 2
factory = ThirdPartyConnectionFactory()
pool = ConnectionPool(factory)
consumer = ConnectionConsumer(pool)
consumer.cycle_new_connection()

assert factory._open_connections == 1
assert factory._opened_connections == 1
print 'Test 2 passing!'

# Test 3
factory = ThirdPartyConnectionFactory()
pool = ConnectionPool(factory)
consumer = ConnectionConsumer(pool)
consumer.cycle_new_connection()
consumer.cycle_new_connection()

assert factory._open_connections == 1
assert factory._opened_connections == 1
print 'Test 3 passing!'

# Test 4
factory = ThirdPartyConnectionFactory()
pool = ConnectionPool(factory)
consumer = ConnectionConsumer(pool)

consumer.cycle_new_connection()

long_open_connection = consumer.open()
consumer.cycle_new_connection()

consumer.assert_open(long_open_connection)
long_open_connection.close()
consumer.assert_closed(long_open_connection)

assert factory._open_connections == 2
assert factory._opened_connections == 2
print 'Test 4 passing!'
