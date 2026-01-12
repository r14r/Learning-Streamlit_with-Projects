import content from '../data/content.json';

const slugify = (value) => value.toLowerCase().replace(/[^a-z0-9]+/g, '-');

export default function Home() {
  return (
    <div className="layout">
      <aside className="sidebar">
        <h1>Learning Streamlit Projects</h1>
        <nav>
          {content.levels.map((level) => (
            <div key={level.id} className="nav-section">
              <a href={`#${slugify(level.id)}`} className="nav-level">
                {level.title}
              </a>
              <ul>
                {level.projects.map((project) => (
                  <li key={project.id}>
                    <a href={`#${slugify(`${level.id}-${project.id}`)}`}>{project.title}</a>
                    <ul>
                      {project.steps.map((step) => (
                        <li key={step.id}>
                          <a href={`#${slugify(`${level.id}-${project.id}-${step.id}`)}`}>
                            {step.filename}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </nav>
      </aside>
      <main className="content">
        {content.levels.map((level) => (
          <section key={level.id} id={slugify(level.id)} className="level">
            <h2>{level.title}</h2>
            {level.projects.map((project) => (
              <section
                key={project.id}
                id={slugify(`${level.id}-${project.id}`)}
                className="project"
              >
                <h3>{project.title}</h3>
                <div className="project-meta">
                  <div>
                    <h4>TODO</h4>
                    <pre>{project.todo || 'No TODO.md provided.'}</pre>
                  </div>
                  <div>
                    <h4>TIPPS</h4>
                    <pre>{project.tipps || 'No TIPPS.md provided.'}</pre>
                  </div>
                </div>
                <div className="steps">
                  {project.steps.map((step) => (
                    <article
                      key={step.id}
                      id={slugify(`${level.id}-${project.id}-${step.id}`)}
                      className="step"
                    >
                      <h4>{step.filename}</h4>
                      <pre>{step.code}</pre>
                    </article>
                  ))}
                </div>
              </section>
            ))}
          </section>
        ))}
      </main>
    </div>
  );
}
