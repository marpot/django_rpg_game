import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Eldoria RPG',
  tagline: 'Django and React RPG based game project',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://marpot.github.io',
  baseUrl: '/django_rpg_game/',

  organizationName: 'marpot', // Twoje GitHub username
  projectName: 'django_rpg_game', // Twoje repozytorium na GitHubie
  deploymentBranch: 'gh-pages', // Branch do GitHub Pages
  trailingSlash: false, // Unikaj końcowego '/'

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'pl',
    locales: ['pl', 'en'], // Dodaj inne języki, jeśli chcesz
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/marpot/django_rpg_game',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/eldoria-social-card.jpg', // Zaktualizuj obrazek nawiązujący do gry
    navbar: {
      title: 'Eldoria RPG',
      logo: {
        alt: 'Eldoria RPG Logo',
        src: 'img/logo.svg', // Wstaw logo swojej gry
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/marpot/django_rpg_game',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            {
              label: 'start',
              to: '/docs/start',
            },
          ],
        },
        {
          title: 'Repository',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/marpot/django_rpg_game',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Eldoria RPG. Built by Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
