import React from "react";
import logo from "./logo.svg";
import "./Global.css";
import "./App.css";
import useSWR from "swr";

// This is the component for a creator card.
function PoseCard(props) {
  return (
    <Col className="p-2 m-2 col-6 col-md-4 col-lg-3 col-xl-2">
      <img src={props.img} alt={props.name} className="poses-img" />
      <h2>{props.english_name}</h2>
      <h3>Sanskrit: {props.sanskrit_name}</h3>
    </Col>
  );
}

// This is the creators container
function Poses() {
  const { poseData, error } = useSWR("/api/poses", fetch);

  if (error) return <div>failed to load</div>;
  if (!poseData) return <div>loading...</div>;

  const poseCards = poseData.map((pose, index) => (
    <PoseCard
      sanskrit_name={pose.sanskrit_name}
      img={pose.img}
      engish_name={pose.english_name}
      key={index}
    />
  ));

  return (
    <section className="yoga-poses">
      <h1>Yoga Poses</h1>
      <Container>
        <Row>{poseCards}</Row>
      </Container>
    </section>
  );
}

export { Poses };
