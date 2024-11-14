<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HansPeter21/Downforce_cal">

  <h3 align="center">Abtriebsberechnung</h3>

</div>

<!-- ABOUT THE PROJECT -->
## Über die Berechnung
Dieses Repository wurde erstellt, um einfach Berechnungen mit der Zuhilfenahme des [Bernoulli-Effektes](https://www.leifiphysik.de/mechanik/stroemungslehre/grundwissen/bernoulli-gleichung) zu erstellen. 
- Es wird durch Masserhaltung die Geschwindigkeit bestimmt.
- Durch Impulserhaltung kann die Druckänderung berechnet werden.
- Aus dieser kann mit der Fläche die Abtriebskraft kalkuliert werden.

#### **Gesamtenergie (Bernoulli-Gleichung):**

- \( p_{\text{tot}} = \frac{\rho v^2}{2} + p = \text{const.} \)

##### **Masseerhaltung:**

- \( \dot{m} = \dot{V} \cdot \rho, \quad \rho = \text{const.} \)
- \( \dot{V} = A \cdot \dot{x}, \quad b = \text{const.} \)
- \( \dot{K} = h(x) \cdot \dot{x} = \text{const.} \)
- \( \dot{K_1} = \dot{K_2} = h_1 \cdot v_{\infty} = h_2 \cdot v_2 \)
- \( v_2 = \frac{h_1 \cdot v_{\infty}}{h_2} \)
- \( v_3 = \frac{h_2 \cdot v_2}{h_3} \)

##### **Impulserhaltung:**

- \( \rho_L \cdot \frac{v_{\infty}^2}{2} + p_{\infty} = \rho_L \cdot \frac{v_2^2}{2} + p_2 \)
- \( p_2 = \rho_L \cdot \frac{v_{\infty}^2 - v_2^2}{2} + p_{\infty} \)
- \( \Delta p = p_2 - p_{\infty} \)

##### **Abtriebskraft:**

- Abtriebskraft \( = \Delta p \cdot l_U \cdot b \)


<!-- CONTACT -->
## Contact

Mauro Schegg  - mauro.schegg@ost.com

Projekt Link: [https://github.com/HansPeter21/Downforce_cal](https://github.com/HansPeter21/Downforce_cal)
