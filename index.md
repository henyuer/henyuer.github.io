---
layout: home
title: Welcome to My GitHub Pages Site
---

Welcome to my GitHub Pages site! This site is generated using [Jekyll](https://jekyllrb.com/) and hosted on GitHub Pages.

## Recent Posts

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <small>{{ post.date | date_to_string }}</small>
    </li>
  {% endfor %}
</ul>

## About

This is a sample static website generated using Jekyll. You can customize this content in the `index.md` file to match the purpose of your site.

To learn more about how to build your own Jekyll site, check out the [Jekyll documentation](https://jekyllrb.com/docs/).
