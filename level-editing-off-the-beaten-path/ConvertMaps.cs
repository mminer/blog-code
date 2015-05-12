static readonly Dictionary<Color, Tile.Type> colorMap = new Dictionary<Color, Tile.Type>()
{
	{ Color.black, Tile.Type.Block },
	{ Color.white, Tile.Type.Empty },
	{ Color.green, Tile.Type.Moon  },
	{ Color.blue,  Tile.Type.Spawn },
};

/// <summary>
/// Gets a map from an image, where each pixel represents a tile.
/// </summary>
/// <param name="imageMap">Image-based map.</param>
/// <returns>Level map.</returns>
static Tile.Type[][] LoadMap (Texture2D imageMap)
{
	var map = new Tile.Type[imageMap.height][];
	var pixels = imageMap.GetPixels();

	for (int row = 0; row < imageMap.height; row++) {
		map[row] = new Tile.Type[imageMap.width];

		for (int col = 0; col < imageMap.width; col++) {
			var pixel = pixels[row * imageMap.width + col];
			map[row][col] = colorMap[pixel];
		}
	}

	return map;
}
