import React from "react";
import "./Global.css";
import "./App.css";
import useSWR from "swr";

// This is an individual sequence
function IndividualSequence() {
  const { individualSequenceData, error } = useSWR("/api/sequences/<sequence_id>/steps", fetch);

  if (error) return <div>failed to load</div>;
  if (!individualSequenceData) return <div>loading...</div>;

  const individualSequenceSteps = individualSequenceData.map((individualStep, index) => (
    <li key="index">{individualStep}</li>
  ));

  return (
    <section className="yoga-poses">
      <h1>{}</h1>
      <Container>
        <Row>
          <ol>
          {individualSequenceSteps}
          </ol>
          </Row>
      </Container>
    </section>
  );
}

export { IndividualSequence };
