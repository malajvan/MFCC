# MFCC-Popularity prediction
Spotify Popularity index prediction algorithm using MFCCs analysis. For more details on my process and application, visit the medium article: [TBU]


## Background
Mel-frequency cepstral coefficients (MFCCs) analysis is a technique widely used for extracting information from audio segments. Recently, it has been applied to music information retrieval, most notably for music genre and feature classifications. This project aims to find a correlation between a track's MFCCs and its popularity, with a focus on the Vietnamese music market.

## Data 
I used Spotipy to retrieve information (name, artist, popularity) of 500 Vietnamese songs and used youtube-dl to download the respective mp3 files. The songs information is in [this file](tbu).

## Methods
I used librosa to calculate the 40 MFCCs for each song ([code](mp3/mfcc.py)) and use sklearn's KNeighborsClassifier to predict song's popularity into four bins: low, med, medhi, high ([code](mp3/prediction_train.py)).

## Discussions


## Authors

Hong Van Pham
[Email], [Linkedin], [Facebook] 


## Acknowledgments
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
