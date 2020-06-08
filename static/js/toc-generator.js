/**
 * Script générant une table des matières
 *
 * @author: Tanguy Cavagna
 * @copyright: Copyright 2020, TPI
 * @version: 1.0.0
 * @date: 2020-06-08
 */
const titles = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
const toc = document.querySelector('.toc');

for (let i = 0; i < titles.length; i += 1) {
    const title = titles[i];
    const tocTitle = document.createElement(title.tagName.toLowerCase());
    const tocLink = document.createElement('a');

    if (!title.hasAttribute('id')) {
        title.id = `h${i}`;
    }
    tocLink.href = `#${title.getAttribute('id')}`;
    tocLink.innerHTML = title.textContent;
    tocTitle.appendChild(tocLink);
    toc.appendChild(tocTitle);
}
