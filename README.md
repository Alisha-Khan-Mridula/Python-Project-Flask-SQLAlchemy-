**Monthly Expense Bill Project V3** 

**Step 1:** Setup the virtual environment  
            
**Step 2:** Factory pattern setup 
        Eliminating Circular Dependency 
        Setup 3 environment that a project has to go through run the project (Setup configuration)
        => DevelopmentConfig 
        => TestingConfig 
        => ProductionConfig 

**Step 3:** Planning all the functions to be done in the project
        =>  Factory pattern configuration function
        =>  Database function
        =>  Logger function
        =>  JWT function
        =>  CORS function
        =>  Swagger function

**Step 4:** Implement the configuration function 
        How to run project in a particular folder: 
        configInfo = os.environ.get(‘CONFIG’)
       [os.environ = contains the environment variable of the current system,
       .get() = used to get/retrieve the value of environment variable,
       ‘CONFIG’ = environment variable ]
       set CONFIG=App.config.DevelopmentConfig 
       [setting the environment variable value,
       App.config = access the folder where DevelopmentConfig function has been defined]

**Step 5:** Implement database creation (Used postman to run the API) 
For creating database: 
engine = create_engine(app.config.get(“DATABASE_URL”))
Session = scorped_session(sessionmaker(bind=engine, autoflash = False, autocommit = False))
Base = declarative_base()
Base.metadata.create_all(bind=engine) 
Step 6: Create the models 
                                                                             


