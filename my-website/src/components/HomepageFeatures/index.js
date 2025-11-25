import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Information Architecture',
    Svg: require('@site/static/img/infoarch.svg').default,
    description: (
      <>
        I can help your organization wrangle your documenation from disparate sources into a single docs-as-code site managed by a static site generator like the one that built this site.
      </>
    ),
  },
  {
    title: 'Writing the Docs',
    Svg: require('@site/static/img/writer.svg').default,
    description: (
      <>
        I can write clear concise docs for any audience on any topic: onboarding, APIs, SDKs, configuration, developer guides, user manuals, test plans, and more.
      </>
    ),
  },
  {
    title: 'Empowering Teams and AI to Build Better Docs',
    Svg: require('@dsite/static/img/editor.svg').default,
    description: (
      <>
        I am an experiences teacher trainer who is passionate about enabling teams to produce better code by producing better documentation with the help of templates, tutorials, and AI tools.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
