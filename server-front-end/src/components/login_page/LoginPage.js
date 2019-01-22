import React, { Component } from 'react';
import './LoginPage.css'

class LoginPage extends Component {
	render() {
		return (
			<div className="container">
				<div className="row loginClass " >
				<div className="col-lg"></div>
					<div className="card loginClass left col-lg-5" >
						<div className="card-body">
							<h5 className="card-title">Card title</h5>
							<h6 className="card-subtitle mb-2 text-muted">Card subtitle</h6>
							<p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
						</div>
					</div>
					<div className="card loginClass right col-lg-5" >
						<div className="card-body">
							<h5 className="card-title">Card title</h5>
							<h6 className="card-subtitle mb-2 text-muted">Card subtitle</h6>
							<p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
						</div>
					</div>
					<div className="col-lg"></div>
				</div>

			</div>
		);
	}
}

export default LoginPage;