# HOWTO Publish a Website

This guide explains how to publish a simple static website using GitHub Pages.

## Steps

1. **Create your website files**: We have created an `index.html` file in the root of the repository as an example.
2. **Create a GitHub Actions Workflow**: In the `.github/workflows` directory, create a workflow file (like `publish-website.yml`) that triggers on pushes to the `main` branch.
3. **Configure the Workflow**: The workflow should check out the code, set up the environment, and use an action like `peaceiris/actions-gh-pages` or the native GitHub Pages deploy action to push the static files to the `gh-pages` branch or directly to GitHub Pages.
4. **Enable GitHub Pages**: In your repository settings, go to the "Pages" section and select "GitHub Actions" as the source, or select the `gh-pages` branch.

Your website will then be available at your GitHub Pages URL!