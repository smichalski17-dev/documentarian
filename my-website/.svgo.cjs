module.exports = {
  multipass: true,
  plugins: [
    { name: 'removeMetadata' },
    { name: 'removeTitle' },
    { name: 'removeDesc' },
    { name: 'removeComments' },
    { name: 'removeEditorsNSData' },
    { name: 'removeEmptyAttrs' },
    { name: 'removeHiddenElems' },
    { name: 'removeEmptyText' },
    { name: 'cleanupAttrs' },
    { name: 'cleanupNumericValues', params: { floatPrecision: 2 } },
    { name: 'convertPathData', params: { floatPrecision: 2 } },
    { name: 'collapseGroups' },
    { name: 'convertStyleToAttrs' },
  ],
};
