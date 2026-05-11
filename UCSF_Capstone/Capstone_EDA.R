library(tidyverse)
library(tableone)

data <- read.csv('srm_longi_12172024.csv')

#formatting
data$msex <- factor(data$msex,
                    levels = c(0,1),
                    labels = c('Female', 'Male'))

data$cogdx_3gp <- factor(data$cogdx_3gp,
                         levels = c(1,2,3),
                         labels = c('Normal', 'MCI', 'Dementia'))

data$race7 <- factor(data$race7,
                     levels = c(1:7),
                     labels = c('White', 
                                'Black or African American', 
                                'American Indian or Alaska Native',
                                'Native Hawaiian or Other Pacific Islander',
                                'Asian',
                                'Other',
                                'Unknown'))

data$c_score <- factor(data$c_score,
                       levels = c(0:3),
                       labels = c('No neuritic plaques', 
                                  'Sparse neuritic plaques', 
                                  'Moderate neuritic plaques',
                                  'Frequent neuritic plaques'))

#isolate just peptide data from dataset
uppercase_cols <- grep("^[A-Z]", names(data), value = TRUE)

tau_cols <- grep("^tau_", names(data), value = TRUE)

bA_cols <- grep("^bA", names(data), value = TRUE)
print(data[, bA_cols])

peptide_cols <- unique(c(uppercase_cols, tau_cols, bA_cols))

#Only 1 visit per person
data_peptides <- data[, peptide_cols] |>
  distinct(ProjID, .keep_all = TRUE)
  

#stage frequency
status_table <- table(data$cogdx_3gp)

status_df <- data.frame(status_table)

colnames(status_df)[1] <- 'Status'

ggplot(
  data=status_df,
  aes(x = Status, y = Freq, fill = Status)) +
  geom_bar(stat = 'identity') +
  labs(title = 'Prevalence of Each Stage',
       x = 'Status',
       y = 'Count') +
  theme_minimal()

#distribution of races

data |>
  distinct(projid, .keep_all = TRUE) |>
  group_by(race7) |>
  summarise(n_race = n())
#almost 98% of participants are white (shocker)

#education: educ (yrs of education)
data |>
  distinct(projid, .keep_all = TRUE) |> 
  group_by(cogdx_3gp) |>
  summarize(mean_education = mean(educ, na.rm = TRUE)) |>
  ggplot(aes(x = cogdx_3gp, y = mean_education, fill = cogdx_3gp)) +
  geom_bar(stat = 'identity') +
  labs(x = 'Cognitive Status', y = 'Mean Years of Education') +
  theme_minimal()
#years of education is almost identical between all stages
#likely reflects racial bias in dataset - white ppl get more education on average, regardless of cognitive stage
  

#age at death: age_death
data |>
  distinct(projid, .keep_all = TRUE) |>
  group_by(cogdx_3gp) |>
  summarize(mean_age_death = mean(age_death, na.rm = TRUE))
#again, mean age at death is very similar across all 3 stages - although slight increase as severity increases
#white people -> better access to healthcare, more likely to live longer

#MMSE: cts_estmmse30 (<26 impaired)

data |>
  filter(cts_estmmse30 < 26, na.rm = TRUE) |>
  distinct(projid, .keep_all = TRUE) |>
  group_by(cogdx_3gp) |>
  summarize(n_impaired = n()) |>
  ggplot(aes(x = cogdx_3gp, y = n_impaired, fill = cogdx_3gp)) +
  geom_bar(stat = 'identity') +
  labs(title = 'Impaired Individuals by Cognitive Status',
       x = 'Cognitive Status', 
       y = 'Count') +
  theme_minimal()
#MMSE impaired status significantly increases with worsening cognitive status


#baseline
data_baseline <- data |>
  filter(fu_year == 0)


#baseline characteristics
vars <- c('msex', 'race7', 'age_death', 'educ', 'cts_estmmse30', 'c_score', 'cogn_global')

table1 <- CreateTableOne(vars=vars, strata = 'cogdx_3gp', data = data_baseline, test = TRUE)

print(table1)

