/**
 * This is a script meant to be run interactively at https://jklaczpokemon.wordpress.com/
 * to extract the decklist with images in format needed for other scripts
 * in this folder.
 */

/* Inspect the decklist images gallery ID from the page
 * and call function extract with it.
 */

let extract = (gallery_id) => {
  let gallery = document.querySelector(`#${gallery_id}`);

  let decklist = gallery.previousElementSibling.querySelectorAll("tr")[1];

  let counts = Array.from(decklist.querySelectorAll("td")).flatMap((td) => {
    cards = td.textContent.split("\n");
    return cards.map((card) => {
      return card.match(/(\d+)x.*/)[1];
    });
  });

  let srcs = Array.from(gallery.querySelectorAll("img")).map((img) =>
    img.src.replace(/\?.*/, "")
  );

  let output = counts.map((count, idx) => `${count} ${srcs[idx]}`);

  console.log(output.join("\n"));
};
