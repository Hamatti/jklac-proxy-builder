# PTCG Proxies from Jason Klaczynski's blog

A collection of scripts and outputs to print out proxies of old formats

Each format is in its own folder and each deck likewise so.

## How to use

### `extract.js`

`extract.js` is a Javascript used in developer tools console when on [Jason's blog](https://jklaczpokemon.wordpress.com/).

First, you need to find the deck you want to proxy. Inspect the gallery of pictures with the dev tools and find the gallery ID.

Create a new variable

```js
let GALLERY_ID = "[your gallery id here]";
```

and then copy-paste and run the script.

Store the output of the script into `images.txt` in your deck's subfolder.

### `build.py`

After using `extract.js`, navigate into the deck's folder and run

```
python ../../build.py images.txt > index.html
```

which will generate the HTML page for printing.
