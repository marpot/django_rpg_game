import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'RPG Game in Django and React',
    description: (
      <>
        Our RPG game was built using Django and React to provide the best gaming experience.
      </>
    ),
  },
  {
    title: 'Game Mechanics',
    description: (
      <>
        The game mechanics include combat and character development.
      </>
    ),
  },
  {
    title: 'Multiplayer Mode',
    description: (
      <>
        Play with friends and other players in our multiplayer mode.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx(styles.feature, 'col')}>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row justify-content-center">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}