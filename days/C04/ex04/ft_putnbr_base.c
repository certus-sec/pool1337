/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sboukhel <sboukhel@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/17 14:01:59 by sboukhel          #+#    #+#             */
/*   Updated: 2026/08/17 21:29:52 by sboukhel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	check_base(char *base)
{
	int	i;
	int	j;

	i = 0;
	if (!base[0] || !base[1])
	{
		return (0);
	}
	while (base[i] != '\0')
	{
		j = i + 1;
		while (base[j] != '\0')
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		if (base[i] == '-' || base[i] == '+' || base[i] <= 32 || base[i] == 127)
		{
			return (0);
		}
		i++;
	}
	return (i);
}

void	ft_putnbr_base(int nbr, char *base)
{
	int			base_len;
	long int	nb;

	nb = nbr;
	base_len = check_base(base);
	if (base_len == 0)
		return ;
	if (nb == 0)
	{
		write(1, &base[0], 1);
		return ;
	}
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
	}
	if (nb >= base_len)
		ft_putnbr_base((nb / base_len), base);
	write(1, &base[nb % base_len], 1);
}
