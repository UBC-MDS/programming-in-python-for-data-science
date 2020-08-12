    def truncate(
        self: FrameOrSeries, before=None, after=None, axis=None, copy: bool_t = True
    ) -> FrameOrSeries:

        if axis is None:
            axis = self._stat_axis_number
        axis = self._get_axis_number(axis)
        ax = self._get_axis(axis)

        # GH 17935
        # Check that index is sorted
        if not ax.is_monotonic_increasing and not ax.is_monotonic_decreasing:
            raise ValueError("truncate requires a sorted index")

        # if we have a date index, convert to dates, otherwise
        # treat like a slice
        if ax.is_all_dates:
            from pandas.core.tools.datetimes import to_datetime

            before = to_datetime(before)
            after = to_datetime(after)

        if before is not None and after is not None:
            if before > after:
                raise ValueError(f"Truncate: {after} must be after {before}")

        if ax.is_monotonic_decreasing:
            before, after = after, before

        slicer = [slice(None, None)] * self._AXIS_LEN
        slicer[axis] = slice(before, after)
        result = self.loc[tuple(slicer)]

        if isinstance(ax, MultiIndex):
            setattr(result, self._get_axis_name(axis), ax.truncate(before, after))

        if copy:
            result = result.copy()

        return result




        """
        Truncate a Series or DataFrame before and after some index value.
        This is a useful shorthand for boolean indexing based on index
        values above or below certain thresholds.
        Parameters
        ----------
        before : date, str, int
            Truncate all rows before this index value.
        after : date, str, int
            Truncate all rows after this index value.
        axis : {0 or 'index', 1 or 'columns'}, optional
            Axis to truncate. Truncates the index (rows) by default.
        copy : bool, default is True,
            Return a copy of the truncated section.
        Returns
        -------
        type of caller
            The truncated Series or DataFrame.
        See Also
        --------
        DataFrame.loc : Select a subset of a DataFrame by label.
        DataFrame.iloc : Select a subset of a DataFrame by position.
        Notes
        -----
        If the index being truncated contains only datetime values,
        `before` and `after` may be specified as strings instead of
        Timestamps.
        Examples
        --------
        >>> df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'],
        ...                    'B': ['f', 'g', 'h', 'i', 'j'],
        ...                    'C': ['k', 'l', 'm', 'n', 'o']},
        ...                   index=[1, 2, 3, 4, 5])
        >>> df
           A  B  C
        1  a  f  k
        2  b  g  l
        3  c  h  m
        4  d  i  n
        5  e  j  o
        >>> df.truncate(before=2, after=4)
           A  B  C
        2  b  g  l
        3  c  h  m
        4  d  i  n
        The columns of a DataFrame can be truncated.
        """





        