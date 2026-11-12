# Marketing distribution drafts

Platform-specific drafts for manually posting a canonical article (one written on
stephencollins.tech or in this repo's own `blog/`) to other platforms. Nothing here is
auto-published — every file is copied and pasted by hand, with the noted canonical-URL
step applied where the platform supports one.

## Layout

```
marketing/
  social/           Platform-native posts: no canonical-URL field, just a link out
    hacker-news/    <YYYY-MM-DD-slug>.md — submission title/URL + suggested author comment
    x/              <YYYY-MM-DD-slug>.md — numbered tweet thread
    linkedin/       <YYYY-MM-DD-slug>.md — single post
  publications/     Full-length syndicated reposts: platform supports a canonical-URL field
    medium/         <YYYY-MM-DD-slug>.md — set via Story settings or "Import a story"
    hashnode/       <YYYY-MM-DD-slug>.md — `canonicalUrl` frontmatter field, pre-filled
```

`<YYYY-MM-DD-slug>` matches the date and slug of the canonical post being distributed, so a
single post's drafts across platforms are easy to find by searching the filename. Add a new
platform as its own subfolder under `social/` or `publications/` rather than inventing a new
top-level layout.

## Status tracking

Each platform folder holds drafts regardless of whether they've been posted yet — this repo
doesn't track publish status (no `gh`/API access from here); check the platform itself for
whether a given draft has gone out.
