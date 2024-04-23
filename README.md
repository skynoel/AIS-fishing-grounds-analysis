# AIS-fishing-grounds-analysis
Use AIS data to analyze potential fishing grounds
## introduction
Analyze AIS files that have completed time code processing to find potential fishing grounds  
It is divided into the following five steps  
1. MAD
2. PATD
3. CHR_PATD
4. ASD
5. PFG
### MAD
Distinguish the preprocessed AIS data between Channel A and Channel B, and count the number of packets per minute. Once you know the number of packets per minute for the channel, you can draw the average packet average for each hour of the day (Message Average Diagram, MAD) , and the "average packet volume per minute" for daily, monthly, and yearly statistics is used for subsequent calculation processing.  
### PATD
The MAD value is converted into a daily Packet Active Time Diagram (PATD). The purpose is to determine when further analysis is required. The PATD judgment result is displayed in green (i.e. the value is 1).   
### CHR_PATD
The results of applying "CH Rules" to PATD are further processed. The purpose of this process is to prevent a certain period to be processed from being excluded from ASD processing because the average MAD value is slightly lower than the threshold, resulting in key information. omission. Therefore, if the time period meets the "Qihe Rules", it will be included in the ASD processing queue.  
### ASD
Through the number of packets in a specific period and the ship type TYPE OF SHIP, the MMSI code belonging to the fishing vessel is filtered, and the fishing vessel whose speed (SOG) does not exceed 2 knots (Class-A) or 3 knots (Class-B) is further filtered. Dynamic data are collected and imported into hexagonal cells (cells) with a diameter of about 500 meters that are pre-divided in a geographic information system (GIS). Know which cell (and its cell ID) these fishing boats are located in, and count the number of fishing boat dynamic messages (Area Signal Density, ASD) per hour in these cells, and then re-import the results into QGIS to present (Potential Fishing Ground, PFG) picture  
### PFG
Then the ASD indicator is used to indicate the concentration of fishing boats in different sea areas. According to the information in "IALA 1082: An Overview of AIS", the AIS table determines the transmission rate. When the speed of Class-A shipborne equipment is less than 3 knots (or the speed of Class-B shipborne equipment is less than 2 knots), the dynamic data The transmission frequency is changed to every 3 minutes. Therefore, if the ASD indicator of a certain hexagonal cell is between 50125 in one hour, it should be equivalent to 36 ships operating in this cell after conversion. Communities with ASD index values ​​above the threshold value of 50 can be regarded as PFG. These communities represent areas where fishing boats carrying out light fishing are more frequent.  
## note
ASD and PFG still not completed