# Theoretical Basics

Version 1

## Delta and Gamma

In the context of financial derivatives pricing and risk management, Delta and Gamma are key "Greeks" used to measure the sensitivity of an option's value to changes in the underlying asset. Delta represents the rate of change of the option price with respect to changes in the underlying asset price, effectively capturing the directional exposure of a position. Gamma, on the other hand, measures the rate of change of Delta itself, indicating how stable or unstable the Delta is as the underlying price fluctuates. Understanding and managing Delta and Gamma is essential for constructing effective hedging strategies and controlling risk exposure in derivatives portfolios.

## Dynamic Hedging

The predictive power of GEX is essentially driven by the necessity of option dealers' (market makers') re-hedging activities. In order to limit risk and realize profit, an option market-maker must limit his exposure to delta. If, e.g., a market-maker sells a single, 20-delta put contract to an investor, he must then short-sell approximately 20 shares of the underlying stock in order to (temporarily) neutralize the convexity effect of the option's gains and losses. Since the convexity itself cannot be hedged away, the market maker must commit to re-hedging the option to its new delta whenever the underlying price changes enough to justify action. If in one case the price of the underlying falls and the put delta rises from 20 to 50, the market-maker will be compelled to short-sell an additional 30 shares of the underlying to stay delta-neutral. If instead the underlying rises and the put delta falls to 0, the market-maker would buy back the previously shorted shares. Thus, a market-maker is essentially committed to a predictable and quantifiable regimen of buying and selling stock.

## Effect of Dealer’s Dynamic Hedging

<table>
  <thead>
    <tr>
      <th>Option Dealers' Opening Interest</th>
      <th>Long Put</th>
      <th>Short Put</th>
      <th>Long Call</th>
      <th>Short Call</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Underlying</td>
      <td>Long S</td>
      <td>Short S</td>
      <td>Short S</td>
      <td>Long S</td>
    </tr>
    <tr>
      <th>Price Movements</th>
      <th colspan="4">Dynamic Hedging</th>
    </tr>
    <tr>
      <td>S Up</td>
      <td>Short S</td>
      <td>Short S</td>
      <td>Short S</td>
      <td>Short S</td>
    </tr>
    <tr>
      <td>S Down</td>
      <td>Long S</td>
      <td>Long S</td>
      <td>Long S</td>
      <td>Long S</td>
    </tr>
    <tr>
      <th colspan="5">Impact of Dynamic Hedging</th>
    </tr>
    <tr>
      <td>Impact to S movements</td>
      <td>Curb</td>
      <td>Promote</td>
      <td>Curb</td>
      <td>Promote</td>
    </tr>
  </tbody>
</table>

## Four Assumptions

The size and liquidity of the equity option market is what makes it possible to glean predictive information from the impact of hedging activity, but it also introduces some challenges. With a few assumptions, we attempt to overcome those challenges:

- All traded options are facilitated by delta-hedgers. This is to say that every option contract is either bought by, or sold by, a market participant whose business is to profitably manage a book of options.
- Call options are sold by investors; bought by market-makers. It is difficult to determine the “direction” of a trade in an ultra-liquid market, as in the case of SPX options. A vast majority will trade at the midpoint of the bid and ask. It is apparent from an analysis of skew, open interest at strike, and (circularly) the effects of GEX, however, that the practice of call overwriting (and stock collaring) drives the market for calls.
- Put options are bought by investors; sold by market-makers. As with calls, puts are primarily used by investors who are already exposed to the underlying market, and who are looking to modify the return pro5le of their portfolio by using options. The “protective put” commands a premium for this reason, thus influencing the apparent vertical skew of index options.
- Market-makers hedge precisely to the option delta. If market-makers hedged their deltas every time an option's delta changed, they would be trading incessantly. In reality, market-makers utilize “hedging bands” to balance the twin challenges of hedging costs and delta risk. Since it is not feasible to gauge the breadth of every market-maker's hedging band, we simply use the delta of the option.

With these assumptions we can compute GEX.
