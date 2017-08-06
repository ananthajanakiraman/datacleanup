# @begin Data_Cleanup @desc Workflow for cleaning up data in farmersmarkets.csv using OpenRefine.
# @in farmersmarkets.csv @desc farmersmarkets.csv
# @param transform_fm_json 

    # @begin run_openrefine_farmersmarkets_dataset @desc farmersmarkets dataset  \n Columns Updated : FMID, MarketName, street, city, County, State, zip, \n Season1Date, Season1Time, Season2Date, Season2Time, Season3Date, Season3Time, \nSeason4Date, Season4Time, x into Latitude, y into Longitude, Location, Credit, WIC, WICcash, SFMNP, SNAP, \n Organic, Bakedgoods, Cheese, Crafts, Flowers, Eggs, Seafood, Herbs, \nVegetables, Honey, Jams, Maple, Meat, Nursery, \nNuts, Plants, Poultry, Prepared, Soap, Trees, Wine, Coffee, Beans, Fruits, Grains, \n Juices, Mushrooms, PetFood, Tofu, WildHarvested, updateTime \n Columns Deleted : Facebook, Youtube, Twitter, Website and Other media

    # @param farmersmarkets.csv
    # @param transform_fm_json @uri file:farmersmarketJSON.json
    # @out cleaned_up_fm_file @uri file:run/run_log.txt
    # @end run_openrefine_farmersmarkets_dataset

    # @begin run_sqlite_farmersmarkets_dataset @desc Additional cleanup on farmersmarkets.csv
    # @in cleaned_up_fm_file 
    # @param sql_farmersmarkets_file @uri file:farmersmarketsclup.sql
    # @out final_fm_file @uri file:run/run_log.txt
    # @end run_sqlite_farmersmarkets_dataset
    
    print("Data Cleanup")

# @end Data_Cleanup