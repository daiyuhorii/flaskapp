class SystemConfig:

  DEBUG = True

  URI = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    "testuser",
    "testuser",
    "localhost",
    "db20191129"
  )

Config = SystemConfig