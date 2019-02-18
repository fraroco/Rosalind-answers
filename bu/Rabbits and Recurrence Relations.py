long rabbitPairs(5, 5) {
    if (numMonths == 1) {
        return 1;
    }
    else if (numMonths == 2) {
        return numOffspring;
    }
    long oneGen = rabbitPairs(numMonths — 1, numOffspring);
    long twoGen = rabbitPairs(numMonths — 2, numOffspring);
    if (numMonths <= 4) {
        return (oneGen + twoGen);
    }
    return (oneGen + (twoGen * numOffspring));
}