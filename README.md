**Monthly Expense Bill Project V3** 

**Step 1:** Setup the virtual environment  </br>
            
**Step 2:** Factory pattern setup </br> 
        Eliminating Circular Dependency </br>
        Setup 3 environment that a project has to go through run the project (Setup configuration)</br>
        => DevelopmentConfig </br>
        => TestingConfig </br>
        => ProductionConfig </br>

**Step 3:** Planning all the functions to be done in the project</br>
        =>  Factory pattern configuration function</br>
        =>  Database function</br>
        =>  Logger function</br>
        =>  JWT function</br>
        =>  CORS function</br>
        =>  Swagger function</br>

**Step 4:** Implement the configuration function </br>
        How to run project in a particular folder: </br>
        configInfo = os.environ.get(‘CONFIG’)</br>
       [os.environ = contains the environment variable of the current system,</br>
       .get() = used to get/retrieve the value of environment variable,</br>
       ‘CONFIG’ = environment variable ]</br></br>
       set CONFIG=App.config.DevelopmentConfig </br>
       [setting the environment variable value,</br>
       App.config = access the folder where DevelopmentConfig function has been defined]</br>

**Step 5:** Implement database creation (Used postman to run the API) </br>
For creating database: </br>
engine = create_engine(app.config.get(“DATABASE_URL”))</br>
Session = scorped_session(sessionmaker(bind=engine, autoflash = False, autocommit = False))</br>
Base = declarative_base()</br>
Base.metadata.create_all(bind=engine) </br>
Step 6: Create the models 
                                                                             


