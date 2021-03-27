import React from "react";
import "./Global.css";
import "./App.css";
import useSWR from "swr";

// This is only the user's sequences, it is rendering as links.
function UserSequences() {

  const { userSequencesData, error } = useSWR("/api/user/<user_id>/savedsequences", fetch);

  if (error) return <div>failed to load</div>;
  if (!userSequencesData) return <div>loading...</div>;

  // If the user already had some sequences saved
  if (userSequencesData) {
    const sequenceCards = userSequenceData.map((sequence, index) => (
      <Col className="col-12 col-md-4 col-lg-2">
        <Link to="/sequences/<sequence_id>">
        {sequence.sequence_name} {sequence.length > 50 ? "45-70 minutes" : "20-40 minutes"}
        </Link>
      </Col>
    ))

  return (
    {sequenceCards}
  );
    }
  // If the user has not saved any sequence cards, this will render instead of sequences links.  
  else {
    return (<p>Please check out popular sequences or create your own with our sequence generator!</p>);
  };

}

// This is the user entire container.
function User() {


  const { userData, error } = useSWR("/api/user", fetch);

  if (error) return <div>failed to load</div>;
  if (!userData) return <div>loading...</div>;

  return (
    <section className="about-the-creators">
      <h1>Welcome {userData.first_name}</h1>
      <Container className="p-5 m-5 translate-middle d-flex justify-content-center">
        <Row className="translate-middle">Full Name: {userData.first_name} {userData.last_name}</Row>
        <Row className="translate-middle">Level: {userData.level}</Row>
        <Row className="translate-middle">Email: {userData.email}</Row>
        <Row className="translate-middle">My Sequences:</Row>
        <Row className="translate-middle">My Sequences:</Row>
      </Container>
    </section>
  );
}

export { User };
