# The Melodies of Politics
In order to replicate this study, please complete the following steps:
1.	You must first create a spotify developer application by going to https://developer.spotify.com/ and clicking dashboard. Once you have logged in using your Spotify account you can move onto step 2.
2.	Create an app by clicking on the greyed-out box that says “My New App” and giving the app a name and description and agreeing to the terms and conditions
3.	Download the sample code from https://github.com/spotify/web-api-auth-examples and replace app.js with the code from Appendix E. NOTE: Remember to put your Client ID and Client Secret (found in your Developer Spotify App) and the ip address/website you plan on using to host the survey into the app.js code where it says ‘INSERT YOUR URI’, at this point you can also input the callback url to your Spotify app.
4.	Create a webpage using html to replace index.html found in authorization_code/public/ to work with the study, make sure to include the button code in Appendix D in your html file in order to obtain the Spotify data.
5.	In the callback page for your website, include the link to your survey with a number that counts up every time Spotify data is submitted to match the data saved to your computer/hostserver
6.	Run the site (with app.js) whilst distributing the survey to obtain Spotify data
7.	Once satisfied with the number of responses, close the survey and close the program.
8.	In a new folder, save files with the code from Appendices F-J
9.	Run the raw spotify data through the code from Appendices F and H.*
10.	After running that raw data, run the new data through Appendices G and I.*
11.	Take the final data in indAtts and input the json files into Excel using the Get Data -> JSON found in the Data tab
12.	Take the final data in indGenres and input it by pasting each text file.
13.	Use the calculations from Appendix A for the survey data and make the necessary correlational tests
*Note: for steps 10 and 11, no other preparation other than having all the files necessary in the correct places should be needed, if an error occurs, reference the code for file structures.
