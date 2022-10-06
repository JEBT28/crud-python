import psycopg2 as pg

class connection: 
    _host=''
    _port=''
    _db=''
    _user=''
    _password=''
    _conn = None
    
    def __init__(self,host,port,db,user,password):
        self._host=host
        self._port=port
        self._db=db
        self._user=user
        self._password=password
        
    def connect(self):
        if self._conn is None:
            self._conn = pg.connect(host=self._host, port=self._port, database=self._db, user=self._user, password=self._password)
            print("Conectado a la base de datos")
        
    def getCursor(self):
        if self._conn is None:
            self.connect()
        return self._conn.cursor()
    
    def getConnection(self):
        if self._conn is None:
            self.connect()
        return self._conn
    
    def commit(self):
        self._conn.commit()
    
    def close(self):
        if self._conn.cursor() is not None:
            self._conn.cursor().close()
        
        if self._conn is not None:
            self._conn.close()
            self._conn = None