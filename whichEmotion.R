
# Import llibrary/package -------------------------------------------------

library(tidyverse)

# Import data files -------------------------------------------------------

df <-
    list.files(path = "./data/", # Set working directory to the dir /emotion-test/
               pattern = "*.csv", 
               full.names = T) %>% 
    map_df(~read_csv(., col_select = c('mouse.clicked_name', 'textNote.text', 'participant'),
                     col_types = cols(.default = "c")))


# Rename column names -----------------------------------------------------

df <- df %>% rename(emotion = mouse.clicked_name, note = textNote.text, user = participant)

df$emotion <- str_remove_all(df$emotion, "\\[|\\]|\'") # Clean the participant's response


# Get the emotion expressed by the users -----------------------------------

print(df) # Each column represents the emotional state of each user
 


# R version 4.2.2 (2022-10-31) // platform: aarch64-apple-darwin20      


