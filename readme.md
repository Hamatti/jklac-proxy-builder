# PTCG Proxies from Jason Klaczynski's blog

## NOTICE

Jason's blog has changed its layout and this project does not work anymore.

The best way to build proxies from Jason's blog now is to use the **Copy deck list** button, then head over to [https://limitlesstcg.com/tools/proxies](https://limitlesstcg.com/tools/proxies), choose **List input** and paste the list there.

## Original Readme

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

### `index.py`

`index.py` is used for generating an index page on the top level for all the decks you have inside.

```
python index.py > index.html
```
