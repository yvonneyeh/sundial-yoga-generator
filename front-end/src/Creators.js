import React from "react";
import "./Global.css";
import "./App.css";
import useSWR from "swr";
import { Row, Col, Container } from "react-bootstrap";

// This is the component for a creator card.
// pass in props - some stuff
function CreatorCard(props) {
  return (
    <Col className="p-2 m-2 col-12 col-md-6">
      <img src={props.img} alt={props.name} className="creator-img" />
      <h2>{props.name}</h2>
      <ul>
        <li>
          <a href="{props.linkedin}" target="_blank">
            LinkedIn
          </a>
        </li>
        <li>
          <a href="{props.github" target="_blank">
            Git Hub
          </a>
        </li>
      </ul>
      <p>{props.about}</p>
    </Col>
  );
}

// This is the creators entire container
function Creators() {
  // USE SWR
  const { creatorData, error } = useSWR("/api/creators", fetch);

  if (error) return <div>failed to load</div>;
  if (!creatorData) return <div>loading...</div>;


  const creatorCards = creatorData.map((creator, index) => (
    <CreatorCard
      name={creator.name}
      img={creator.img}
      github={creator.github}
      linkedin={creator.linkedin}
      about={creator.about}
      key={index}
    />
  ));

  return (
    <section className="about-the-creators">
      <h1>About the Creators</h1>
      <Container className="p-5 m-5 translate-middle d-flex justify-content-center">
        <Row className="translate-middle">{creatorCards}</Row>
      </Container>
    </section>
  );
}

export { Creators };
