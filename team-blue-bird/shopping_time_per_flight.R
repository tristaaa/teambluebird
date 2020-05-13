#setwd("C:/Users/gamic/Downloads/drive-download-20200416T210553Z-001")
setwd("C:/Users/gamic/Downloads/drive-download-20200422T063540Z-001")
library(dplyr)
library(sqldf)
#flight_similarity <- read.csv("flight_similarity_1.csv", stringsAsFactors = F)
#flight_similarity <- read.csv("flight_similarity_all_passengers.csv", stringsAsFactors = F)
flight_similarity <- read.csv("all_flight_passengers.csv", header = F)
flight_similarity <- flight_similarity[-1,]
flight_similarity_1 <- flight_similarity[1:562249,]
flight_similarity_1 <- flight_similarity_1[,c("V2", "V5", "V6", "V7", "V9", "V10", "V11")]
flight_similarity_2 <- flight_similarity[562250:nrow(flight_similarity),]
flight_similarity_2 <- flight_similarity_2[, c("V2", "V3", "V4", "V5", "V9", "V10", "V11")]
colnames(flight_similarity_1) <- c("Gate", "Arrival", "Date", "Schedule_Depart_Time", "x_dept", "mac_id", "similarity")
colnames(flight_similarity_2) <- c("Gate", "Arrival", "Date", "Schedule_Depart_Time", "x_dept", "mac_id", "similarity")
flight_similarity <- rbind(flight_similarity_1, flight_similarity_2)
#tst0 <- read.csv("tst0.csv", header = T)
#tst1 <- read.csv("tst11.csv", header = T)
#tst2 <- read.csv("tst12.csv", header = T)
#tst3 <- read.csv("tst21.csv", header = T)
#tst4 <- read.csv("tst22.csv", header = T)
#tst5 <- read.csv("tst3.csv", header = T)
#tst6 <- read.csv("tst4.csv", header = T)
#tst7 <- read.csv("tst5.csv", header = T)
tst0 <- read.csv("tst_new0.csv", header = T)
tst1 <- read.csv("tst_new1.csv", header = T)
tst2 <- read.csv("tst_new2.csv", header = T)
tst3 <- read.csv("tst_new3.csv", header = T)
tst4 <- read.csv("tst_new4.csv", header = T)
tst5 <- read.csv("tst_new5.csv", header = T)
#mac_id_shopping <- bind_rows(tst0, tst1, tst2, tst3, tst4, tst5, tst6, tst7)
mac_id_shopping <- bind_rows(tst0, tst1, tst2, tst3, tst4, tst5)
mac_id_shopping <- mac_id_shopping[,c(2,3)]
colnames(mac_id_shopping) <- c("mac_id", "V2")
flight_shopping <- inner_join(mac_id_shopping, flight_similarity)
flight_shopping <- flight_shopping[flight_shopping$similarity > .1,]
flight_shopping$estimated_time <- flight_shopping$V2*flight_shopping$similarity
flight_shopping_final <- sqldf("Select Gate, Arrival, Date, Schedule_Depart_Time, Actual_Depart_Time, Actual_Arrival_Time, Flying_Hours, sum(estimated_time) From flight_shopping Group By Gate, Arrival, Date, Schedule_Depart_Time, Actual_Depart_Time, Actual_Arrival_Time, Flying_Hours")
flight_shopping_final$Schedule_Depart_Time <- 24*flight_shopping_final$Schedule_Depart_Time
flight_shopping_final$Actual_Depart_Time <- 24*flight_shopping_final$Actual_Depart_Time
write.csv(flight_shopping_final, "flight_shopping_10_percent.csv", row.names = F)

library(ggplot2)
ggplot(data = flight_similarity) + geom_histogram(aes(x = similarity, fill = Gate))
ggplot(data = flight_similarity) + geom_violin(aes(x = Arrival, y = similarity))
common_destinations = flight_similarity[flight_similarity$Arrival %in% c("Amsterdam", "Atlanta", "Buenos Aires", "Cordoba", "Frankfurt", "Houston", "Lima", "Lisbon", "London", "Madrid", "Miami", "Panama City", "Paris", "Rome", "Rosario", "Santiago"), ]
ggplot(data = common_destinations) + geom_bar(aes(x = Arrival, y = similarity), stat = "summary", fun.y = "mean") + labs(y = "Average Certainty") + geom_hline(yintercept = mean(flight_similarity$similarity, na.rm = T), color = 'red')
common_gates =flight_similarity[flight_similarity$Gate %in% c("C44", "C46", "C47", "C49", "C50", "C51", "C53", "C54", "C55", "C56", "C59", "C61", "C62", "C63", "C64", "C65", "C66", "C67", "C69"), ]
ggplot(data = common_gates) + geom_bar(aes(x = Gate, y = similarity), stat = "summary", fun.y = "mean") + labs(y = "Average Certainty") + geom_hline(yintercept = mean(flight_similarity$similarity, na.rm = T), color = 'red')
flight_shopping <- read.csv("flight_shopping.csv")

common_destinations = flight_shopping[flight_shopping$Arrival %in% c("Amsterdam", "Atlanta", "Buenos Aires", "Cordoba", "Frankfurt", "Houston", "Lima", "Lisbon", "London", "Madrid", "Miami", "Panama City", "Paris", "Rome", "Rosario", "Santiago"), ]
ggplot(data = common_destinations) + geom_bar(aes(x = Arrival, y = sum.estimated_time.), stat = "summary", fun.y = "mean") + labs(y = "Average Shopping Time") + geom_hline(yintercept = mean(common_destinations$sum.estimated_time., na.rm = T), color = 'red')
common_gates =flight_shopping[flight_shopping$Gate %in% c("C44", "C46", "C47", "C49", "C50", "C51", "C53", "C54", "C55", "C56", "C59", "C61", "C62", "C63", "C64", "C65", "C66", "C67", "C69"), ]
ggplot(data = common_gates) + geom_bar(aes(x = Gate, y = sum.estimated_time.), stat = "summary", fun.y = "mean") + labs(y = "Average Shopping Time") + geom_hline(yintercept = mean(common_gates$sum.estimated_time., na.rm = T), color = 'red')

passengers_per_flight <- sqldf("select Gate, Arrival, Date, Schedule_Depart_Time, sum(similarity) as Estimated_Passengers from flight_similarity group by Gate, Arrival, Date, Schedule_Depart_Time")
write.csv(passengers_per_flight, "Passengers_per_flight.csv", row.names = F)
passengers_per_Destination <- sqldf("Select Arrival, avg(Estimated_Passengers) from passengers_per_flight group by Arrival")
write.csv(passengers_per_Destination, "Passengers_per_destination.csv", row.names = F)
passengers_per_gate <- sqldf("Select Gate, avg(Estimated_Passengers) from passengers_per_flight group by Gate")
passengers_per_flight$Schedule_Depart_Time = floor(passengers_per_flight$Schedule_Depart_Time*24)
passengers_per_time <- sqldf("Select Schedule_Depart_Time, avg(Estimated_Passengers) from passengers_per_flight group by Schedule_Depart_Time")
write.csv(passengers_per_time, "passengers_per_time.csv", row.names = F)


passengers_per_destination <- read.csv("Passengers_per_destination.csv")
x <- toJSON(passengers_per_destination, pretty = T)
ten_percent <- read.csv("flight_shopping_10_percent.csv")
ten_percent$Flying_Hours <- as.character(ten_percent$Flying_Hours)
ten_percent$Flying_Hours <- paste(ten_percent$Flying_Hours, ":00", sep="")
ten_percent$Flying_Hours <- chron(times=(ten_percent$Flying_Hours))
ten_percent <- ten_percent[!is.na(ten_percent$Flying_Hours),]
flying_hours_dest <- sqldf("select Arrival, AVG(Flying_Hours) from ten_percent group by Arrival")
flying_hours_dest$`AVG(Flying_Hours)` <- flying_hours_dest$`AVG(Flying_Hours)`*24
colnames(flying_hours_dest) <- c("Arrival", "avg.Flying_Hours")
y <- toJSON(flying_hours_dest, pretty = T)
