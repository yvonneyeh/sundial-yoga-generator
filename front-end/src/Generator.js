import React from "react";
import "./Global.css";
import "./App.css";
import useSWR from "swr";

// This is an individual sequence
function GeneratorSequence() {
  const { generatedSequence, error } = useSWR("/api/random-sequence/", fetch);

  if (error) return <div>failed to load</div>;
  if (!generatedSequence) return <div>loading...</div>;

  const generatedSequenceSteps = generatedSequence.map((individualStep, index) => (
    <li key="index">{individualStep}</li>
  ));

  return (
    <section className="yoga-sequence">
      <h1>{}</h1>
      <Container>
        <Row>
          <ol>
          {generatedSequenceSteps}
          </ol>
          </Row>
          <Row>
            <button>Love it</button>
            <button>Try Again</button>
            </Row>
      </Container>
    </section>
  );
}

export { GenorateSequence };
