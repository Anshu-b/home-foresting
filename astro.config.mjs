import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";
export default defineConfig({
   site: 'http://anshu-b.github.io/home-foresting/',
  integrations: [tailwind(),  sitemap()],
  base: "/home-foresting"

});