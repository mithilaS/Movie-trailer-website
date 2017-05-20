import media
import fresh_tomatoes

toy_story = media.Movie("TOY Story","A story of a boy and his toys that come alive",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "Toy Stor Youtube link")




avatar = media.Movie("Avatar", "A marine on an alient planet" ,
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")



inception = media.Movie("Inception","An architect of a dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=GuW4X4Gwq2w")

shrek = media.Movie("Shrek" ,"A green ogre named Shrek rescues princess Fiona and fell in love with her",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=ooJJX3R42WM")

the_imitation_game = media.Movie("The imitation game","During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg","https://www.youtube.com/watch?v=S5CjKEFb-sM")



movies =[toy_story,avatar,inception,shrek,the_imitation_game]
print(media.Movie.__module__)
#fresh_tomatoes.open_movies_page(movies)