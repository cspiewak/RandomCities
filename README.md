# RandomCities
This is a random island map generator for City Skylines. Though you could probably use it for other games that use the same type of height map. It will make an 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines. The map is generated not by anything fancy (e.g. Perlin Noise map), but you should pretty much always get a unique map to play with. The generated map will be an island drawn mostly inside the buildable area.

Just generate the heightmap, and import it to City Skylines in the Map Editor with your favorite theme. Then just add two highway connections that don't go anywhere at the edge of the map (one in, one out). Adjust the sea level to your preference. Add boat and air connections (main ways for people to get to the island). The last thing you need to do is to make sure that your starting area has water.

I would recommend that you use these generated maps with a mod that lets you buy all areas.

This is a simple script, but it gets the job done. Time to start looking at ways to generate more natural topology.
