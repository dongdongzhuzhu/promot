import random
from random import choice
medium = ["photograph","35mm film photograph","agfacolor photograph","ambrotype photograph",
"calotype photograph","collodion glass plate photograph","cyanotype photograph",
"daguerreotype photograph","disposable camera photograph","depth map photograph",
"expired film photograph","expired polaroid","film negative photograph","glamor photography",
"hyperspectral imaging","infrared photography","instax photograph","knolling photograph",
"kodachrome photograph","lomography photograph","night vision photograph","paparazzi photograph",
"photogram photograph","pinhole photograph","polaroid photograph","portrait photograph","product photograph",
"sepia photograph","silhouette photograph","tilt-shift lens photograph","tintype photograph","trail cam photograph",
"ultraviolet photograph","vintage film photograph"]
film = ["2001 A Space Odyssey","A Clockwork Orange","Adaptation","Amelie",
"American Graffiti","Apocalypse Now","Arrival","Being John Malkovich","Birdman",
"Blade Runner","Brazil","Citizen Kane","City of God","Dark Knight","Dogville","Drive",
"Dune","Enemy","Enter the Void","Eraserhead","Eternal Sunshine Of The Spotless Mind","Fargo",
"Gravity","Hook","Interstellar","It","La La Land","Labyrinth","Life of Pi","Mad Max Fury Road",
"Metropolis","Momento","Neon Demon","Oblivion","Only God Forgives","Paprika","Pleasantville",
"Psycho","Pulp Fiction","Spirited Away","Star Wars","Stranger Things","Suspiria","The Artist",
"The Cell","The Fall","The Grand Budapest Hotel","The Joker","The Nightmare Before Christmas",
"The Revenant","The Shape of Water","The Tree of Life","TRON","What Dreams May Come","Who Framed Roger Rabbit"]

camera =["super-resolution microscopy","microscopy","macro lens","pinhole lens",
"first person view","wide angle lens","ultra-wide angle lens","fisheye lens","telephoto lens",
"panorama","360 panorama","tilt-shift lens","telescope view","drone view","aerial","from above",
"satellite imagery","blurry","bokeh","ICM","long exposure","motion blur","soft focus","8mm lens",
"35mm lens","50mm lens","80mm lens","200mm lens","500mm lens"]

color = ["white","black","red","cyan","brown","dark-red","dark-cyan","dark-brown",
"light-red","light-cyan","light-brown","black and white","complementary color","cool color",
"dark color","dichromatism color","faded color","high contrast","inverted color","light color",
"low contrast","monochromatic color","muted color","neon color","pantone color","pastel color",
"rainbow color","saturated color","sepia color","spectral solar","vibrant color","vivid color","warm color",
"RGB","CMYK","1-bit grayscale","4-bit grayscale","3-bit color","6-bit color","technicolor","spring colors",
"summer colors","autumn colors","winter colors","camouflage color","confetti color","diffraction pattern color",
"disco color","funky color","gradient color","halftone color","polka dot color","pop-art color","purity color",
"spectrum color","synesthesia color","tie-dye color","35mm film color","agfacolor color","ambrotype color",
"bokeh color","calotype color","chromatic aberration color","collodion glass plate color","cyanotype color",
"daguerreotype color","depth map color","expired film color","expired polaroid","film negative color","fujifilm digital",
"hyperspectral imaging color","kodachrome color","instax color","kodak gold 200 film color","lomography color","night vision color",
"photogram color","polaroid color","sepia photograph color","tintype color","tri-x 400 tx color","ultraviolet color",
"vignette color","vintage film color"]
light = ["bright lighting","campfire lighting","candlelight","cinematic lighting","colorful lighting",
"contre-jour lighting","dark lighting","dramatic lighting","early morning lighting","film noir lighting",
"golden hour sunlight","hard lighting","moody lighting","night lighting","realistic lighting",
"soft lighting","studio lighting","sunset lighting","volumetric lighting","backlight","bioluminescence",
"black light bulb","candle light","christmas lights","crepuscular rays","daylight","edison bulb","fire light","floodlight",
"fluorescent bulb","glow in the dark light","glow stick","glowing light","halfrear lighting","infrared light","lantern light",
"laser light","LED lights","lens flare","light rays","natural lighting","neon bulb","nixie tube bulb",
"plasma globe","silhouette lighting","spotlight","sunlight","vacuum tube bulb","x-ray"]
a = choice(medium)
promot = 'portrait of underwood play guitar'+','+choice(medium)+','+choice(film)+','+choice(camera)+','+choice(color)+','+choice(light)
print(promot)
