-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/0m2LvP
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "TotalAccessbydistance_obesity_clean1_data" (
    "State" varchar(64)   NOT NULL,
    "%_Pop.1/2_mile" float   NOT NULL,
    "%_Pop.1_mile" float   NOT NULL,
    "%_Pop.10_miles" float   NOT NULL,
    "%_Pop.20_miles" float   NOT NULL,
    "Poverty_Rate" float   NOT NULL,
    "Obesity_Rate" float   NOT NULL,
    CONSTRAINT "pk_TotalAccessbydistance_obesity_clean1_data" PRIMARY KEY (
        "State"
     )
);

CREATE TABLE "PovertyByState_clean1_data" (
    "State" varchar(64)   NOT NULL,
    "Pop2010" float   NOT NULL,
    "Families_Under_Pover" float   NOT NULL,
    "Obesity_Rate" float   NOT NULL
);

CREATE TABLE "Income_data_and_obesity_data" (
    "State" varchar(64)   NOT NULL,
    "Unemployment_Rate_2021" float   NOT NULL,
    "Median_Household_Income_2021" float   NOT NULL,
    "Obesity_Rate" float   NOT NULL
);

CREATE TABLE "Final_Obesity_Covid_data" (
    "State" varchar(64)   NOT NULL,
    "Population" float   NOT NULL,
    "Covid_Deaths" float   NOT NULL,
    "%Death" float   NOT NULL,
    "%Obesity" float   NOT NULL
);

ALTER TABLE "PovertyByState_clean1_data" ADD CONSTRAINT "fk_PovertyByState_clean1_data_State" FOREIGN KEY("State")
REFERENCES "TotalAccessbydistance_obesity_clean1_data" ("State");

ALTER TABLE "Income_data_and_obesity_data" ADD CONSTRAINT "fk_Income_data_and_obesity_data_State" FOREIGN KEY("State")
REFERENCES "TotalAccessbydistance_obesity_clean1_data" ("State");

ALTER TABLE "Final_Obesity_Covid_data" ADD CONSTRAINT "fk_Final_Obesity_Covid_data_State" FOREIGN KEY("State")
REFERENCES "TotalAccessbydistance_obesity_clean1_data" ("State");

