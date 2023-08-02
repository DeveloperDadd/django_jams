# Django Jams

## MoSCoW

### Must have :
  * Diagrams of schema to show the relationships within the database
  * Use of models and model serialization to be able to manipulate JSON data on the frontend and backend
  * Be able to show full CRUD functionality of the API using thunder client extension
  * Make use of Django REST framework obviously
### Should have :
  * Multiple CRUD operations for multiple tables - at least a minimum of one CRUD operation per table
  * Testing throughout to make sure the views are working properly
  * Clean, informative comments throughout code to explain what is going on
### Could have :
  * Build  a route to allow a user to add a song to a playlist
  * Built routes that accept query parameters to search/filter for data or all models
  * Create a route that filters a list of songs by artist or some other functionality
  * Add a custom field to the API that keeps tracks of most popular songs based on playlist additions
  * HOOK IT UP TO THE FRONT END <- Album art (displayed in center, with previous track to left, and next track to the right, button functionality to change the 'song' and replay type)
### Won't have : 
  * Any C#

## URLs/Views
  * READ - want multiple functions using model serializers to read ALL of the song titles
    - examples :
      - All songs
      - Songs with title and artists on them
      - Songs with title, artists, and what album that recording is on
      - All the playlists belonging to a certain user
  * POST - Be able to send data to the database
    - examples:
      - New user created, so send username, email, and etc. to the database
      - Cover band records a famous song, so add the artist ID to the song_artists table
  * UPDATE - Be able to update and manipulate current data
    - examples:
      - Developer enters a type or mistakenly enters the wrong album name for an artist, needs to be updated    
  * DELETE - Be able to remove existing data from the database if needed
    - examples:
      - User decides to delete their account, so remove it by USING THEIR PRIMARY KEY **DO NOT FORGET**. In turn, remove their playlists, liked songs, etc.
      - User wants to delete a certain playlist they made for an ex-girlfriend, DELETE USING THE PLAYLIST PRIMARY KEY.

# API Structure
  * API will be created using Django Rest functionality. Specifically model serializers.
  * The data will be store in the database as JSON which can be retrieved from specific URLs using view functionality on the backend and also fetched to display data on the front end.
  * Example of JSON data :
    -  { song_id : 1, "song_name": "Lose Yourself", "artist_name": "Eminem", "genre": "rap", "album" : "8 Mile Soundtrack" } 

# Link to [schema](https://dbdiagram.io/d/64c9a57a02bd1c4a5e14cd77)
