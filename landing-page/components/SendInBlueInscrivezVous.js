import React from "react";

export default class SendInBlueInscrivezVous extends React.Component {
  render() {
    return (
      <section id="inscription" className="section lancez-votre-recherche">
        <iframe
          width="540"
          height="723"
          src="https://my.sendinblue.com/users/subscribe/js_id/35zg8/id/1"
          frameBorder="0"
          scrolling="auto"
          allowFullScreen
          style={{
            background: "transparent",
            display: "block",
            marginLeft: "auto",
            marginRight: "auto",
            maXidth: "100%"
          }}
        />
      </section>
    );
  }
}