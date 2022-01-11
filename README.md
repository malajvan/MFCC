# MFCC-Popularity prediction
Spotify Popularity index prediction algorithm using MFCCs analysis. For more details on my process and application, visit the medium article: [TBU]


## Background
Mel-frequency cepstral coefficients (MFCCs) analysis is a technique widely used for extracting information from audio segments. Recently, it has been applied to music information retrieval, most notably for music genre and feature classifications. This project aims to find a correlation between a track's MFCCs and its popularity, with a focus on the Vietnamese music market.

## Data 
I used Spotipy to retrieve information (name, artist, popularity) of 500 Vietnamese songs and used youtube-dl to download the respective mp3 files. The songs information is in [this file](tbu).

## Methods
I used librosa to calculate the 40 MFCCs for each song ([analysis/mp3/mfcc.py](https://github.com/malajvan/MFCC/blob/main/analysis/mp3/mfcc.py)) and use sklearn's KNeighborsClassifier to predict song's popularity into four bins: low, med, medhi, high ([analysis/mp3/prediction_train.py](https://github.com/malajvan/MFCC/blob/main/analysis/mp3/prediction_train.py)).

## Discussions
From the test data set, we obtained an accuracy score of around 0.856 in popularity classification. This shows a that MFCCs can be used in popularity prediction for tracks. For further usage, I'm planning to predict Ngot band ([Wikipedia article in Vietnamese](https://vi.wikipedia.org/wiki/Ng%E1%BB%8Dt_(ban_nhạc))) newest album's popularity prior to its release to predict hit songs and possibly influence how tracks' order as well as promotional strategies. (album is still in the making, to be updated)

## Authors

Hong Van Pham
[Email](vanhongpham01@gmail.com), [Linkedin](https://www.linkedin.com/in/vanhpham/), [Facebook](https://www.facebook.com/hiiamvan)


## Acknowledgments
I have taken inspirations as well as references from these medium posts
* 
