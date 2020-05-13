#setwd("C:/Users/gamic/Downloads")
setwd("/home/b1275813799/fltdepart")
list.of.packages <- c("chron", "future.apply", "dplyr")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(chron)
library(future.apply)
library(dplyr)
plan(multiprocess)
fltdep0 <- read.csv("fltdeparture0.csv", stringsAsFactors = F, header = F)
fltdep1 <- read.csv("fltdeparture11.csv", stringsAsFactors = F, header = F)
fltdep2 <- read.csv("fltdeparture12.csv", stringsAsFactors = F, header = F)
fltdep3 <- read.csv("fltdeparture21.csv", stringsAsFactors = F, header = F)
fltdep4 <- read.csv("fltdeparture22.csv", stringsAsFactors = F, header = F)
fltdep5 <- read.csv("fltdeparture3.csv", stringsAsFactors = F, header = F)
fltdep6 <- read.csv("fltdeparture4.csv", stringsAsFactors = F, header = F)
fltdep7 <- read.csv("fltdeparture5.csv", stringsAsFactors = F, header = F)
fltdep0 <- bind_rows(fltdep0, fltdep1, fltdep2, fltdep3, fltdep4, fltdep5, fltdep6, fltdep7)
fltdep1 <- ""
fltdep2 <- ""
fltdep3 <- ""
fltdep4 <- ""
fltdep5 <- ""
fltdep6 <- ""
fltdep7 <- ""

fltdep0$V6 <- as.POSIXct(fltdep0$V6, tz = "Etc/GMT-3")
fltdep0 <- fltdep0[,-1]
colnames(fltdep0) <- c("Level", "mac_id", "latitude", "longitude", "datetime")
fltdep0$six_hours_ahead <- fltdep0$datetime + 6*60*60
datetimes <- fltdep0$datetime
mac_ids <- fltdep0$mac_id
is_last_record <- function(x,...) sum(datetimes > x["datetime"][[1]] & datetimes < x["six_hours_ahead"][[1]] & mac_ids == x["mac_id"][[1]])==0
index_list<-as.list(1:nrow(fltdep0[]))
fltdep0$is_last_record <- future_sapply(index_list,function(i)is_last_record(fltdep0[i,]))

fltdep <- fltdep0[fltdep0$is_last_record,]
flight_info <- read.csv("flight_info1.csv", header = F)
colnames(flight_info) <- c("Terminal", "Gate", "Departure", "Arrival", "Date", "Schedule_Depart_Time", "Actual_Depart_Time", "Actual_Arrival_Time", "Flying_Hours")
flight_info$Schedule_Depart_Time <- as.character(flight_info$Schedule_Depart_Time)
flight_info$Schedule_Depart_Time <- paste(flight_info$Schedule_Depart_Time, ":00", sep="")
flight_info$Schedule_Depart_Time <- chron(times=(flight_info$Schedule_Depart_Time))
flight_info$Actual_Depart_Time <- as.character(flight_info$Actual_Depart_Time)
flight_info$Actual_Depart_Time <- paste(flight_info$Actual_Depart_Time, ":00", sep="")
flight_info$Actual_Depart_Time <- chron(times=(flight_info$Actual_Depart_Time))


flight_info[flight_info$Gate == "C-50",]$Gate <- "C50"
flight_info[flight_info$Gate == "C-63",]$Gate <- "C63"
flight_info$Gate <- as.character(flight_info$Gate)
flight_info$Date <- as.character(flight_info$Date)
#make table of gates: latitude, longitude
gates <- data.frame("Gate" = c("C44", "C45", "C46", "C47", "C48", "C49", "C50", "C51", "C52", "C53", "C54", "C55", "C56", "C57", "C58", "C59", "C60", "C61", "C62", "C63", "C64", "C65", "C66", "C67", "C68", "C69"), 
                    latitude = c(-22.816784,-22.816784,-22.817355,-22.817355,-22.818000,-22.818000,-22.817268,-22.818244,-22.818244,-22.818844,-22.818844,-22.818901,-22.818901,-22.818780,-22.818780, -22.818691, -22.818691, -22.818466, -22.818466, -22.816956,  -22.817407,  -22.817407, -22.817805, -22.817805, -22.818251, -22.818251),
                    longitude = c(-43.242308, -43.242308,-43.242741,-43.242741,-43.243243,-43.243243, -43.242314, -43.243074, -43.243074, -43.243542, -43.243542, -43.243644, -43.243644, -43.243904, -43.243904, -43.243952, -43.243952, -43.243837, -43.243837, -43.241368, -43.240732, -43.240732, -43.240137, -43.240137, -43.239459, -43.239459))
flight_info <- left_join(flight_info, gates)
flight_info$actual_depart_datetime <- as.POSIXct(paste(flight_info$Date, flight_info$Actual_Depart_Time), format="%m/%d/%Y %H:%M:%S", tz = "Etc/GMT-3")
flight_probabilities <- function(x){
  #gets all flights between 15 minutes and 2 hours
  in_range <- flight_info[flight_info$actual_depart_datetime > (x["datetime"][[1]] ) & flight_info$actual_depart_datetime < (x["datetime"][[1]] + 180*60),]
  if(nrow(in_range) > 0){
    in_range$x_lat <- x[, "latitude"]
    in_range$x_long <- x[, "longitude"]
    in_range$x_dept <- x[, "datetime"]
    in_range$mac_id <- x[, "mac_id"]
    in_range$physical_distance <- sqrt((in_range$latitude - in_range$x_lat)^2 + (in_range$longitude - in_range$x_long)^2)
    in_range$time_difference <- sqrt(as.numeric(in_range$x_dept - in_range$actual_depart_datetime, units = "days")^2)
    phys_mean <- mean(in_range$physical_distance)
    phys_sd <- sd(in_range$physical_distance)
    time_mean <- mean(in_range$time_difference)
    time_sd <- sd(in_range$time_difference)
    in_range$physical_distance <- (in_range$physical_distance - phys_mean)/phys_sd
    in_range$physical_distance <- in_range$physical_distance - min(in_range$physical_distance) + 1
    in_range$time_difference <- (in_range$time_difference - time_mean)/time_sd
    in_range$time_difference <- in_range$time_difference - min(in_range$time_difference) + 1
    in_range$similarity <- 1/sqrt(in_range$time_difference^2 + in_range$physical_distance^2)
    in_range$similarity <- in_range$similarity/sum(in_range$similarity)
    return(in_range[,c(1:9, 15, 16, 19)])
  }
  return(NULL)
}
plan(multiprocess)
final_list <- future_lapply(as.list(1:nrow(fltdep)),function(i)flight_probabilities(fltdep[i,]))
final_list <- final_list[lengths(final_list) != 0]
future_lapply(final_list, function(x) write.table(x, 'flight_similarity.csv'  , append= T, sep=',', col.names = F, row.names = F))

