import netmovies
import media

warcraft = media.Movie("Warcraft", 
					   "Two Worlds. One Home, based on the hit videogame franchise 'Warcraft' by Blizzard Entertainment.",
					   "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg", 
					   "https://www.youtube.com/watch?v=Orw8CZpzIDU")					   

prince_of_persia = media.Movie("Prince of Persia: The Sands of Time",
						   "Prince Dastan must protect a princess and her magical dagger with the power to turn back time from his brother's, the new king's, forces.",
						   "https://upload.wikimedia.org/wikipedia/en/d/df/Prince_of_Persia_poster.jpg", 
						   "https://www.youtube.com/watch?v=9qXlAls2Gv0",)

tomb_raider = media.Movie("Lara Croft: Tomb Raider",
					      "The beautiful and brainy Lara Croft criss-crosses the globe to find an ancient artifact only to find an ancient organization wants the same.",
						  "https://upload.wikimedia.org/wikipedia/en/9/98/Lara_Croft_film.jpg",
						  "https://www.youtube.com/watch?v=cnNBqNb3taw")

tomb_raider2 = media.Movie("Lara Croft Tomb Raider: The Cradle of Life",
						   "Lara Croft is back in the sequel to the smash hit Lara Croft: Tomb Raider",
						   "https://upload.wikimedia.org/wikipedia/en/2/2e/Lara_Croft_Tomb_Raider_-_The_Cradle_of_Life_Poster.png", 
						   "https://www.youtube.com/watch?v=G4bhBabn-wU",)

silent_hill = media.Movie("Silent Hill",
						   "A desperate mother with a sick child ventures to the mysterious town of Silent Hill.",
						   "http://www.gstatic.com/tv/thumb/movieposters/159818/p159818_p_v8_ad.jpg", 
						   "https://www.youtube.com/watch?v=Y2M8iYL8suw",)
						   
doom = media.Movie("Doom",
						   "Dwayne 'The Rock' Johnson stars in this sci fi thriller about a space marine sent to investigate a security breach at a top secret Martian facility.",
						   "http://www.gstatic.com/tv/thumb/movieposters/89656/p89656_p_v8_ad.jpg", 
						   "https://www.youtube.com/watch?v=WAajNPrU_mY",)

resident_evil_apocalypse = media.Movie("Resident Evil: Apocalypse",
						   "The second installment in the cult hit Resident Evil series",
						   "https://upload.wikimedia.org/wikipedia/en/5/50/Resident_evil_apocalypse_poster.jpg", 
						   "https://www.youtube.com/watch?v=7IM9e3yYLzM",)

need_for_speed = media.Movie("Need for Speed",
						   "'Breaking Bad's' Aaron Paul has a need for speed in this fast paced action thriller.",
						   "http://t2.gstatic.com/images?q=tbn:ANd9GcS_hoRU2hxj7QsqhEuwKSGD1e-sm4WuOrgZdLAy3nKMq8yVw-S7", 
						   "https://www.youtube.com/watch?v=u3wtVI-aJuw",)

dungeon_siege = media.Movie("In the Name of the King: A Dungeon Siege Tale",
						   "Jason Statham stars in a fantasy tale about a man in search of his kidnapped wife even as war looms in the land.",
						   "http://www.gstatic.com/tv/thumb/dvdboxart/167292/p167292_d_v8_aa.jpg", 
						   "https://www.youtube.com/watch?v=Q22A9aRrUIw",)					   
						   
						   
						   
movies = [warcraft, prince_of_persia, tomb_raider, tomb_raider2, silent_hill, doom, resident_evil_apocalypse, need_for_speed, dungeon_siege]
# Uses list of movie instances as input to generate the HTML file called netmovies and open it in the browser. 
netmovies.open_movies_page(movies)