// src/App.jsx
import './App.css';
import logo from './assets/Logo_Transparent.png';
import festivalImg from './assets/Festival_Sunset.jpg';
import voyageImg from './assets/Woman_Sunset.jpg';

function App() {
  return (
    <div className="App">
      <header>
        <nav>
          <div className="burger">&#9776;</div>
          <ul className="nav-links">
            <li><a href="#">Contact</a></li>
            <li><a href="#">A propos</a></li>
            <li><a href="#">Aide</a></li>
            <li><button className="login">Se connecter</button></li>
          </ul>
        </nav>

        <div className="logo-section">
          <img src={logo} alt="Logo GrooveNomad" className="logo-img" />
          <h1 className="slogan">Découvre ta musique.<br />Explore ton monde.</h1>
        </div>

        <div className="hero-images">
          <div className="image-block">
            <img src={festivalImg} alt="Festival" />
            <button className="btn-orange">Trouver un festival</button>
          </div>
          <div className="image-block">
            <img src={voyageImg} alt="Voyage" />
            <button className="btn-pink">Créer mon voyage personnalisé</button>
          </div>
        </div>
      </header>

      <section className="about">
        <h2>A propos</h2>
        <p>Groove Nomad, c'est l'agence de voyage nouvelle génération pour les amateurs de musique et d'aventure.</p>
        <div className="features">
          <div className="feature">
            <h3>Festivals</h3>
          </div>
          <div className="feature">
            <h3>Voyages</h3>
          </div>
          <div className="feature">
            <h3>Recommandation personnalisée</h3>
          </div>
        </div>
      </section>

      <section className="destinations">
        <h2>Destinations populaires</h2>
        <div className="cards">
          <div className="card">Image<br />Nom</div>
          <div className="card">Image<br />Nom</div>
          <div className="card">Image<br />Nom</div>
          <div className="card">Image<br />Nom</div>
        </div>
      </section>

      <section className="reviews">
        <h2>Avis clients</h2>
        <div className="review-list">
          <div className="review">Nom<br />★★★★★<br />Commentaire</div>
          <div className="review">Nom<br />★★★★★<br />Commentaire</div>
          <div className="review">Nom<br />★★★★★<br />Commentaire</div>
        </div>
      </section>

      <footer>
        <p>Suivez-nous :</p>
        <div className="social-icons">
          <a href="#">FB</a>
          <a href="#">IG</a>
          <a href="#">X</a>
        </div>
        <p>&copy; 2025 GrooveNomad</p>
      </footer>
    </div>
  );
}

export default App;
